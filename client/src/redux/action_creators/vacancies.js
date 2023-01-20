import axios from 'axios';
import { GET_GENERAL_VACANCIES, GET_GENERAL_VACANCIES_SUCCESS, GET_GENERAL_VACANCIES_ERROR} from "../types";
import { ALL_VACANCIES_API_URL } from '../../utils/backend_api_urls';

export const fetchVacancies = (page = 1, countOnPage) => {
  return async (dispatch) => {
    dispatch({type: GET_GENERAL_VACANCIES});

    try {
      let response = await axios.get(ALL_VACANCIES_API_URL, { params: { page: page } } );
      dispatch({type: GET_GENERAL_VACANCIES_SUCCESS, action: {
        payload: {
          vacancies: response.data.results,
          page: page,
          countOnPage: countOnPage
        }
      }});
    } catch(e) {
      dispatch({type: GET_GENERAL_VACANCIES_ERROR, action: {payload: e.stack}});
    }
  }
}