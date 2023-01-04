import { useState } from "react";
import {
  Anchor,
  Box,
  Button,
  Grommet,
  grommet,
  Header,
  Page,
  Text,
  Nav,
  Footer,
} from "grommet";
import { Moon, Sun } from "grommet-icons";
import { deepMerge } from "grommet/utils";
import AppRouter from "./components/AppRouter";
import { Link } from "react-router-dom";


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

  return (
    <Grommet theme={theme} full themeMode={dark ? "dark" : "light"}>
      <Page>
        <AppBar>
          <Text size="large">Geek Hunter</Text>
          <Nav direction="row" background="brand" pad="medium">
            <Link to="/">Main page</Link>
            <Link to="vacancies">Vacancies</Link>
          </Nav>
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
        <AppRouter></AppRouter>
      </Page>
      <Footer classNema='footer' background="brand" pad="medium">
          <Text>Copyright</Text>
          <Anchor label="About" />
        </Footer>
    </Grommet>
  );
}

export default App;
