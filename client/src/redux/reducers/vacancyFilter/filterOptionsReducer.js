import { FILTER_CITIES, FILTER_EXPIRIENCES, FILTER_GRADES, FILTER_SPECIALITIES, FILTER_STACKTOOLS, FILTER_VALUES_ERROR } from "../../types";

const initialState = {
  cities: [],
  experiences: [],
  grades: [],
  specialities: [],
  stacktools: [],
  salaryFrom: 0,
  salaryTo: 300000,
  salaryStep: 50000,
  canRemote: false,
  error: null,
};

export const filterOptionsReducer = (state = initialState, action) => {
  switch (action.type) {
    case FILTER_CITIES:
      return {...state, cities: [...action.payload]};
    case FILTER_EXPIRIENCES:
      return {...state, experiences: [...action.payload]};
    case FILTER_GRADES:
      return {...state, grades: [...action.payload]};
    case FILTER_SPECIALITIES:
      return {...state, specialities: [...action.payload]};
    case FILTER_STACKTOOLS:
      return {...state, stacktools: [...action.payload]};
    case FILTER_VALUES_ERROR:
      return {...state, error: action.payload};
    default:
      return state;
  }
}