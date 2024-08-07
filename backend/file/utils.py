import pandas as pd
import re


class ReadingExcelFile:
    
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

    def extract_file_info(self):
        df = pd.read_excel(self.file)
        file_info = df.iloc[0][0]
        month, year = self.extract_month_year(file_info)
        fy_start, fy_end = self.extract_fiscal_year(file_info)
        return {'month': month, 'year': year, 'fy_start': fy_start, 'fy_end': fy_end}
    
    def fixing_columns(self):
        df = pd.read_excel(self.file, header=[2])
        df.rename(columns={df.columns[0]: df.iloc[0][0]}, inplace=True)
        df = df.drop(index=0).reset_index(drop=True)
        return df
        
    def cleaning_file(self, df):
        df['id'] = df.index
        df_previous = df[df['General Insurers'].str.contains('Previous', case=False, na=False)]
        df_previous['id'] = df_previous.index - 1
        df_other = df[~df['General Insurers'].str.contains('Previous', case=False, na=False)]
        df_combined = pd.merge(df_other, df_previous, on='id', how='inner', suffixes=('', '_'))
        df_combined.drop(columns=['id'], inplace=True)
        return df_combined
    
    def extract_data(self):
        pass