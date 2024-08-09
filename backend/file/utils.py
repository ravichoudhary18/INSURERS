import pandas as pd
import re


class ReadingExcelFile:
    
    master_file = pd.ExcelFile('/mnt/master/master.xlsx')
    master_sheet = pd.ExcelFile(master_file)
    name_df = master_sheet.parse('name')
    category_df = master_sheet.parse('category')
    lob_df = master_sheet.parse('lob', header=None)
    month_df = master_sheet.parse('month')
    master_join_df = pd.merge(name_df, category_df, on='clubbed_name')
    list_insurance = name_df['insurer'].tolist()
    select_row = lob_df[0].to_list()
        
    def __init__(self, file):
        self.file = file
        
    def extract_month_year(self, text):
        # Define a regex pattern to extract month and year
        pattern = r"(?P<month>\bJanuary|\bFebruary|\bMarch|\bApril|\bMay|\bJune|\bJuly|\bAugust|\bSeptember|\bOctober|\bNovember|\bDecember)\s+(?P<year>\d{4})"

        # Find all matches in the text
        matches = re.findall(pattern, text)

        if not matches:
            return None, None

        # Extract the first match
        month, year = matches[0]
        return month, year
    
    def extract_fiscal_year(self, text):
        # Define a regex pattern to extract fiscal year information
        fy_pattern = r"FY\s+(?P<fy_start>\d{4})-(?P<fy_end>\d{2})"

        # Search for fiscal year pattern in the text
        fy_match = re.search(fy_pattern, text)

        if fy_match:
            fy_start = fy_match.group('fy_start')
            fy_end = fy_match.group('fy_end')
            return fy_start, fy_end

        return None, None
    
    def get_sheet_list(self):
        return pd.ExcelFile(self.file).sheet_names
    
    
    def extract_file_info(self, df):
        file_info = df.iloc[0][0]
        month, year = self.extract_month_year(file_info)
        fy_start, fy_end = self.extract_fiscal_year(file_info)
        return {'month': month, 'year': year, 'fy_start': fy_start, 'fy_end': fy_end}
    
    def remove_nan_row(self, sheet_names):
        df = pd.read_excel(self.file, sheet_name=sheet_names, header=None)
        df.drop(df[df.isna().all(axis=1)].index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df
    
    def fixing_columns(self, df):
        header_row_index = 1
        new_header = df.iloc[header_row_index]
        df = df.drop(header_row_index).reset_index(drop=True)
        df.columns = new_header
        df = df.drop(index=0).reset_index(drop=True)
        df.rename(columns={df.columns[0]: df.iloc[0][0]}, inplace=True)
        return df
        
    def cleaning_file(self, df):
        df = df[~df['General Insurers'].str.contains('Previous', case=False, na=False)]
        df_filtered = df[df['General Insurers'].isin(self.list_insurance)]
        return df_filtered
    
    def extract_data(self, dataframes, year, month, file_instance):
        transformed_data = []

        for dataframe in dataframes:
            dataframe.rename(columns={'General Insurers': 'Product'}, inplace=True)
            intersection_columns = list(set(self.select_row).intersection(set(dataframe.columns)))
            intersection_columns.insert(0, 'Product')
            dataframe = dataframe[intersection_columns]

            dataframe['category'] = dataframe['Product'].apply(
                lambda x: self.master_join_df.loc[self.master_join_df['insurer'] == x, 'category'].iloc[0])
            dataframe['clubbed_name'] = dataframe['Product'].apply(
                lambda x: self.master_join_df.loc[self.master_join_df['insurer'] == x, 'clubbed_name'].iloc[0])

            for _, row in dataframe.iterrows():
                print(row)
                # break
                
                clubbed_name = row['clubbed_name']
                category = row['category']

                for column in row.index:
                    print(column)
                    if column not in ['clubbed_name', 'category', ]:
                        transformed_data.append({
                            'file': file_instance,
                            'year': year,
                            'month': month,
                            'clubbed_name': clubbed_name,
                            'category': category,
                            'product': column,
                            'value': row[column]
                        })

        return transformed_data
