import { React, useState, useEffect } from "react";
import { PageContent, PageHeader, Grid, Spinner } from "grommet";
import Vacancies from "./Vacancies";
import axios from "axios";

const VacanciesListPage = () => {
  const [vacancies, setVacancies] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    async function fetchData() {
      const allVacanciesURL = `http://localhost:8000/vacancies`;
      
      setIsLoading(true);
      let response = await axios.get(allVacanciesURL);

      let vacancyList = response.data.results;
      setVacancies(vacancyList);

      setIsLoading(false);
    }

    fetchData();
  }, []);

  return (
    <PageContent className="page">
      <PageHeader title="Vacancies" />
      <Grid gap="large" pad={{ bottom: "large" }}>
        {isLoading 
        ? <Spinner />
        : <Vacancies vacancies={vacancies}></Vacancies>
        }
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
