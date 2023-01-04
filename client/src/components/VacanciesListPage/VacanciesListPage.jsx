import { React, useState, useEffect } from "react";
import { Box, PageContent, PageHeader, Grid, Spinner, Pagination } from "grommet";
import Vacancies from "./Vacancies";
import axios from "axios";

const VacanciesListPage = () => {
  const [vacancies, setVacancies] = useState([]);
  const [vacanciesCount, setVacanciesCount] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  async function fetchData(currentPage) {
    const allVacanciesURL = `http://localhost:8000/vacancies?page=${currentPage}`;
    
    setIsLoading(true);
    let response = await axios.get(allVacanciesURL);

    let vacancyList = response.data.results;
    let vacancyCount = response.data.count;
    setVacancies(vacancyList);
    setVacanciesCount(vacancyCount);
    setIsLoading(false);
  }
  
  useEffect(() => {
    fetchData(currentPage);
  }, [currentPage]);

  const handleListChange = ({page, startIndex, endIndex}) => {
    setCurrentPage(page);
  }

  return (
    <PageContent>
      <PageHeader title="Vacancies" />
      <Grid gap="large" pad={{ bottom: "large" }}>
        {isLoading 
        ? <Vacancies isLoading={true}></Vacancies>
        : <Vacancies isLoading={false} vacancies={vacancies}></Vacancies>
        }

      <Box justify="center" align="center"> <Pagination page={currentPage} numberItems={vacanciesCount} onChange={handleListChange} /> </Box>
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
