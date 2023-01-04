import { React, useState, useEffect } from "react";
import { PageContent, PageHeader, Grid } from "grommet";
import Vacancies from "./Vacancies";
import axios from "axios";

const VacanciesListPage = () => {
  const [vacancies, setVacancies] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const allVacanciesURL = `http://localhost:8000/vacancies`;
      let response = await axios.get(allVacanciesURL);

      let vacancyList = response.data.results;
      setVacancies(vacancyList);
    }

    fetchData();
  }, []);

  return (
    <PageContent>
      <PageHeader title="Vacancies" />
      <Grid gap="large" pad={{ bottom: "large" }}>
        <Vacancies vacancies={vacancies}></Vacancies>
      </Grid>
    </PageContent>
  );
};

export default VacanciesListPage;
