import VacanciesListPage from "./components/VacanciesListPage/VacanciesListPage";
import VacancyDataPage from "./components/VacancyPage/VacancyDataPage";
import MainPage from "./components/MainPage/MainPage";
import LoginPage from "./components/Authorization/LoginPage";
import { LOGIN_ROUTE, MAIN_PAGE_ROUTE, VACANCIES_LIST_ROUTE, VACANCY_ROUTE } from "./utils/consts";


export const authRoutes = [

]

export const publicRoutes = [
  {
    path: VACANCIES_LIST_ROUTE + VACANCY_ROUTE + '/:id',
    Component: VacancyDataPage,
  },
  {
    path: MAIN_PAGE_ROUTE,
    Component: MainPage,
  },
  {
    path: VACANCIES_LIST_ROUTE,
    Component: VacanciesListPage,
  },
  {
    path: LOGIN_ROUTE,
    Component: LoginPage,
  },
  
]