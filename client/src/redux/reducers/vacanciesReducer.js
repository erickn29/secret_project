import { GET_GENERAL_VACANCIES, GET_GENERAL_VACANCIES_SUCCESS, GET_GENERAL_VACANCIES_ERROR} from "../types";

const initialState = {
  vacancies: [],
  loading: false,
  error: null,
  allVacanciesCount: 10,
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
        allVacanciesCount: action.payload.allVacanciesCount,
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