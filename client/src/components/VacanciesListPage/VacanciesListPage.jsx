import { React, useState, useEffect } from "react";
import { Box, PageContent, PageHeader, Grid, Pagination, Sidebar, Avatar, Spinner } from "grommet";
import Vacancies from "./Vacancies";
import VacancyListFilter from "../Filters/VacancyListFilter";
import { useSelector, useDispatch } from "react-redux";
import { fetchVacancies } from "../../redux/action_creators/vacancies";

const VacanciesListPage = () => {
  const {vacancies, loading, error, page, countOnPage} = useSelector(state => state.vacanciesReducer);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchVacancies());
  }, []);

  return (
    <PageContent>
      <PageHeader alignSelf="center" title="Список вакансий" />
      <VacancyListFilter></VacancyListFilter>
      <Grid gap="large" pad={{ bottom: "large" }}>
        { loading ? <Spinner /> : <Vacancies /> }
        <Box justify="center" align="center"> 
          <Pagination page={page} numberItems={countOnPage}/> 
        </Box>
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
