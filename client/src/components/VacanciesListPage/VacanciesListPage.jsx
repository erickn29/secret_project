import { React, useState, useEffect } from "react";
import { Box, PageContent, PageHeader, Grid, Pagination, Sidebar, Avatar, Spinner, Text } from "grommet";
import Vacancies from "./Vacancies";
import VacancyListFilter from "../Filters/VacancyListFilter";
import { useSelector, useDispatch } from "react-redux";
import { fetchVacancies } from "../../redux/action_creators/vacancies";
import { PAGINATION_SET_COUNT_ON_PAGE, PAGINATION_SET_PAGE } from "../../redux/types";

const VacanciesListPage = () => {
  const {vacancies, loading, error, allVacanciesCount} = useSelector(state => state.vacanciesReducer);
  const {page, countOnPage} = useSelector(state => state.paginationReducer);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchVacancies(page, countOnPage));
  }, [page, countOnPage]);

  const pageChangeHandler = ({ page, startIndex, endIndex }) => {
    dispatch({type: PAGINATION_SET_PAGE, payload: page});
  }

  return (
    <PageContent>
      <PageHeader alignSelf="center" title="Список вакансий" />
      {/* <VacancyListFilter></VacancyListFilter> */}
      <Grid gap="large" pad={{ bottom: "large" }}>
        { loading ? <Spinner /> : <Vacancies /> }
        <Box align="center" direction="row" justify="between">
          <Text>
            Всего {allVacanciesCount}
          </Text>
          <Pagination page={page} numberItems={allVacanciesCount} step={countOnPage} onChange={pageChangeHandler}/> 
        </Box>
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
