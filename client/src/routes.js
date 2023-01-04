import VacanciesListPage from "./components/VacanciesListPage/VacanciesListPage";
import VacancyData from "./components/VacancyPage/VacancyData";
import MainPage from "./components/MainPage/MainPage";
import { MAIN_PAGE_ROUTE, VACANCIES_LIST_ROUTE, VACANCY_ROUTE } from "./utils/consts";


export const authRoutes = [

]

export const publicRoutes = [
  {
    path: VACANCIES_LIST_ROUTE + VACANCY_ROUTE + '/:id',
    Component: VacancyData,
  },
  {
    path: MAIN_PAGE_ROUTE,
    Component: MainPage,
  },
  {
    path: VACANCIES_LIST_ROUTE,
    Component: VacanciesListPage,
  },
  
]