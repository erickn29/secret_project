import { useState, useEffect, useContext } from "react";
import Vacancies from "./components/VacanciesList/Vacancies";

import axios from "axios";
import {
  Box,
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Grid,
  Grommet,
  grommet,
  Header,
  Heading,
  Page,
  PageContent,
  PageHeader,
  Paragraph,
  ResponsiveContext,
  Text,
} from "grommet";
import { Moon, Sun } from "grommet-icons";
import { deepMerge } from "grommet/utils";
// require('dotenv').config();

const theme = deepMerge(grommet, {
  global: {
    colors: {
      brand: "#228BE6",
    },
    font: {
      family: "Roboto",
      size: "18px",
      height: "20px",
    },
  },
});

const AppBar = (props) => (
  <Header
    background="brand"
    pad={{ left: "medium", right: "small", vertical: "small" }}
    elevation="medium"
    {...props}
  />
);

function App() {
  const [dark, setDark] = useState(false);
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
    <Grommet theme={theme} full themeMode={dark ? "dark" : "light"}>
      <Page>
        <AppBar>
          <Text size="large">Geek Hunter</Text>
          <Button
            a11yTitle={dark ? "Switch to Light Mode" : "Switch to Dark Mode"}
            icon={dark ? <Moon /> : <Sun />}
            onClick={() => setDark(!dark)}
            tip={{
              content: (
                <Box
                  pad="small"
                  round="small"
                  background={dark ? "dark-3" : "light-3"}
                >
                  {dark ? "Switch to Light Mode" : "Switch to Dark Mode"}
                </Box>
              ),
              plain: true,
            }}
          />
        </AppBar>
        <PageContent>
          <PageHeader title="Vacancies" />
          <Grid gap="large" pad={{ bottom: "large" }}>
            <Vacancies vacancies={vacancies}></Vacancies>
          </Grid>
        </PageContent>
      </Page>
    </Grommet>
  );
}

export default App;
