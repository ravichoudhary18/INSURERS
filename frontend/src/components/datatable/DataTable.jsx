import React, { useState } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TablePagination, Paper, Button } from '@mui/material';
import { styled } from '@mui/material/styles';
import { tableCellClasses } from '@mui/material/TableCell';
import useAxiosPrivate from '../../hooks/useAxiosPrivate';

const DataTable = ({ data, id }) => {

  const axiosPrivate = useAxiosPrivate()

  const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: theme.palette.common.black,
      color: theme.palette.common.white,
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 14,
    },
  }));

  const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
      border: 0,
    },
  }));

  // Pagination states
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);

  // Handle page change
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  // Handle rows per page change
  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  // Slice data for current page
  const paginatedData = data.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage);

  // Extract headers from data object keys
  const headers = Object.keys(data[0]).splice(0, 6);
  
  const downloadHandler = async (event) => {
    try {
    const response = await axiosPrivate.get(`/file/file-download/${id}/`, {
      responseType: 'blob',
    })
    const blob = new Blob([response.data]);
    const url =  window.URL.createObjectURL(blob);
    
    // Create an anchor element and click it to trigger the download
    const a = document.createElement('a');
    a.href = url;
    a.download = 'report.xlsx'; // Specify the default filename
    document.body.appendChild(a);
    a.click();
    
    // Clean up
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error downloading the file:', error);
  }
  } 
  

  return (
    <div style={{ maxHeight: '80vh', width: '80%', margin: 'auto' }}>
      <Paper>
        <TableContainer>
        <Button type='button' onClick={downloadHandler} variant="contained" color="success">
            Download
          </Button>
          <TablePagination
            rowsPerPageOptions={[5, 10, 25]}
            component="div"
            count={data.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
          <Table stickyHeader aria-label="sticky table">
            <TableHead>
              <TableRow>
                {headers.map(header => (
                  <StyledTableCell key={header}>{header.replace('_', ' ').toUpperCase()}</StyledTableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {paginatedData.map((row, rowIndex) => (
                <StyledTableRow key={rowIndex}>
                  {headers.map((header, cellIndex) => (
                    <StyledTableCell key={cellIndex}>
                      {row[header]}
                    </StyledTableCell>
                  ))}
                </StyledTableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </div>
  );
};


export default DataTable;