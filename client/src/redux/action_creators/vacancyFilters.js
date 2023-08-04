import axios from 'axios';
import { FILTER_CITIES, FILTER_EXPIRIENCES, FILTER_GRADES, FILTER_SPECIALITIES, FILTER_VALUES_ERROR } from "../types";
import { FILTER_LIST_CITIES_API_URL, FILTER_LIST_EXPERIENCES_API_URL, FILTER_LIST_GRADES_API_URL, FILTER_LIST_SPECIALITIES_API_URL } from '../../utils/backend_api_urls';

export const fetchFilterValues = () => {
  return async (dispatch) => {
    
    try {
      let responseCities = await axios.get(FILTER_LIST_CITIES_API_URL);
      
      dispatch({type: FILTER_CITIES, 
        payload: responseCities.data.result,
      });

      let responseExperiences = await axios.get(FILTER_LIST_EXPERIENCES_API_URL);
      
      dispatch({type: FILTER_EXPIRIENCES, 
        payload: responseExperiences.data.result,
      });

      let responseGrades = await axios.get(FILTER_LIST_GRADES_API_URL);
      
      dispatch({type: FILTER_GRADES, 
        payload: responseGrades.data.result,
      });

      let responseSpecialities = await axios.get(FILTER_LIST_SPECIALITIES_API_URL);
      
      dispatch({type: FILTER_SPECIALITIES, 
        payload: responseSpecialities.data.result,
      });

      // let responseStacktools = await axios.get(FILTER_LIST_STACKTOOLS_API_URL);
      
      // dispatch({type: FILTER_STACKTOOLS, 
      //   payload: responseStacktools.data.results,
        
      // });
    } catch(e) {
      dispatch({type: FILTER_VALUES_ERROR, 
          payload: e.name,
        }
      );
    }
  }
}
