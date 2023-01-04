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
import { useNavigate } from "react-router-dom";

// require('dotenv').config();

const theme = deepMerge(grommet, {
  global: {
    colors: {
      brand: "#7D4CDB",
      defaultText: "#F8F8F8",
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
  const navigate = useNavigate();

  return (
    <Grommet theme={theme} full themeMode={dark ? "dark" : "light"}>
      <Page>
        <section className="wrapper">
          <header className="wrapper__header">
            <AppBar>
              <div className="appbar__left">
                <Text
                  className="main-logo-title"
                  size="large"
                  onClick={() => navigate("/")}
                >
                  Geek Hunter
                </Text>
              </div>
              <div
                style={{ display: "flex", flexDirection: "row" }}
                className="appbar_right"
              >
                <Nav direction="row" background="brand" pad="medium">
                  <Anchor
                    onClick={() => navigate("vacancies")}
                    label="Vacancies"
                    color="defaultText"
                  />
                  <Anchor
                    onClick={() => navigate("login")}
                    label="Login"
                    color="defaultText"
                  />
                </Nav>
                <Button
                  a11yTitle={
                    dark ? "Switch to Light Mode" : "Switch to Dark Mode"
                  }
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
              </div>
            </AppBar>
          </header>

          <main className="wrapper__content">
            <AppRouter></AppRouter>
          </main>

          <footer className="wrapper__footer">
            <Footer background="brand" pad="medium">
              <Text>Copyright</Text>
              <Anchor label="About" color="defaultText" />
            </Footer>
          </footer>
        </section>
      </Page>
    </Grommet>
  );
}

export default App;
