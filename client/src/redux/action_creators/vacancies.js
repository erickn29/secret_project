import axios from 'axios';
import { GET_GENERAL_VACANCIES, GET_GENERAL_VACANCIES_SUCCESS, GET_GENERAL_VACANCIES_ERROR} from "../types";
import { ALL_VACANCIES_API_URL, FILTER_VACANCIES_API_URL } from '../../utils/backend_api_urls';

export const fetchVacancies = (page = 1, countOnPage = 10, filterData) => {
  return async (dispatch) => {
    dispatch({type: GET_GENERAL_VACANCIES,});

    console.log(filterData);
    let response;

    try {
      // if (true) {
      //   response = await axios.get(ALL_VACANCIES_API_URL, { params: { page: page,  } } );
      // } 
      
      if (true) {
        response = await axios.get(FILTER_VACANCIES_API_URL, { params: { page: page, location: filterData.city, salary_from: filterData.chosenSalaryFrom, is_remote: filterData.isRemote === true ? 1 : 0 } } );
      }
      
      dispatch({type: GET_GENERAL_VACANCIES_SUCCESS, 
        payload: {
          vacancies: response.data.results,
          page: page,
          countOnPage: countOnPage,
          allVacanciesCount: response.data.count,
        }
      });
    } catch(e) {
      dispatch({type: GET_GENERAL_VACANCIES_ERROR, 
          payload: e.name,
        }
      );
    }
  }
}