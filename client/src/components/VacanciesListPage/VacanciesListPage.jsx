import { React, useState, useEffect } from "react";
import { Box, PageContent, PageHeader, Grid, Pagination } from "grommet";
import Vacancies from "./Vacancies";
import VacancyListFilter from "../Filters/VacancyListFilter";
import { useScrollTo } from "react-use-window-scroll";
import axios from "axios";

const VacanciesListPage = () => {
  const [vacancies, setVacancies] = useState([]);
  const [vacanciesCount, setVacanciesCount] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  const scrollTo = useScrollTo();

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
    console.log('scrollTo')
    scrollTo(0, 0);
    fetchData(currentPage);
  }, [currentPage]);

  const handleListChange = ({page, startIndex, endIndex}) => {
    setCurrentPage(page);
  }

  return (
    <PageContent>
      <PageHeader alignSelf="center" title="Список вакансий" />
      <VacancyListFilter></VacancyListFilter>
      <Grid gap="large" pad={{ bottom: "large" }}>
        {isLoading 
        ? <Vacancies isLoading={true}></Vacancies>
        : <Vacancies isLoading={false} vacancies={vacancies}></Vacancies>
        }

        <Box justify="center" align="center"> 
          <Pagination page={currentPage} numberItems={vacanciesCount} onChange={handleListChange} /> 
        </Box>
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
