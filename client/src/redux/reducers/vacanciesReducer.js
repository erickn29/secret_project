import { GET_GENERAL_VACANCIES, GET_GENERAL_VACANCIES_SUCCESS, GET_GENERAL_VACANCIES_ERROR} from "../types";

const initialState = {
  vacancies: [],
  loading: false,
  error: null,
  page: 1,
  countOnPage: 10,
};


export const vacanciesReducer = (state = initialState, action) => {

  switch (action.type) {
    case GET_GENERAL_VACANCIES:
      return {
        ...state,
        loading: true,
      };
    case GET_GENERAL_VACANCIES_SUCCESS:
      return {
        loading: false,
        error: null,
        vacancies: [...action.payload.vacancies],
        page: action.payload.page,
        countOnPage: action.payload.countOnPage,
      };
    case GET_GENERAL_VACANCIES_ERROR:
      return {
        ...state,
        loading: false,
        error: action.payload,
      };
    default:
      return {...state};
  }
}