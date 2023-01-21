import axios from 'axios';
import { GET_GENERAL_VACANCIES, GET_GENERAL_VACANCIES_SUCCESS, GET_GENERAL_VACANCIES_ERROR} from "../types";
import { ALL_VACANCIES_API_URL, FILTER_VACANCIES_API_URL } from '../../utils/backend_api_urls';

export const fetchVacancies = (page = 1, countOnPage = 10, filterData) => {
  return async (dispatch) => {
    dispatch({type: GET_GENERAL_VACANCIES,});

    console.log(filterData);

    // const generateReqParams = (filterData) => {
    //   const queryParams = {};

    //   queryParams.page = page;

    //   if ('city' in filterData && filterData.city) {
    //     queryParams.location = filterData.city;
    //   }

    //   if ('chosenSalaryFrom' in filterData && filterData.chosenSalaryFrom) {
    //     queryParams.salary_from = filterData.chosenSalaryFrom;
    //   }

    //   if ('isRemote' in filterData  && filterData.isRemote) {
    //     queryParams.is_remote = filterData.isRemote === true ? 1 : 0;
    //   }

    //   if ('experience' in filterData && filterData.experience) {
    //     queryParams.experience = filterData.experience.join(',');
    //   }

    //   if ('speciality' in filterData  && filterData.speciality) {
    //     queryParams.speciality = filterData.speciality.join(',');
    //   }

    //   if ('grade' in filterData  && filterData.grade) {
    //     queryParams.grade = filterData.grade.join(',');
    //   }

    //   return queryParams;
    // };

    try {

      let response = await axios.get(FILTER_VACANCIES_API_URL, { params: { 
        page: page, 
        location: filterData.city, 
        salary_from: filterData.chosenSalaryFrom ? filterData.chosenSalaryFrom : null, 
        is_remote: filterData.isRemote ? (filterData.isRemote === true ? 1 : 0) : null,
        experience: filterData.experience ? filterData.experience.join(',') : null,
        speciality: filterData.speciality ? filterData.speciality.join(',') : null,
        grade: filterData.grade ? filterData.grade.join(',') : null,
      } } );
   
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