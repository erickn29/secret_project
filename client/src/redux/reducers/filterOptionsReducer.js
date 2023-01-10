import { FILTER_CITIES, FILTER_EXPIRIENCES, FILTER_GRADES, FILTER_SPECIALITIES, FILTER_STACKTOOLS } from "../types";

const initialState = {};

export const filterOptionsReducer = (state = initialState, action) => {
  switch (action.type) {
    case FILTER_CITIES:
      return {...state, cities: [...action.payload]};
    case FILTER_EXPIRIENCES:
      return {...state, expiriences: [...action.payload]};
    case FILTER_GRADES:
      return {...state, grades: [...action.payload]};
    case FILTER_SPECIALITIES:
      return {...state, specialities: [...action.payload]};
    case FILTER_STACKTOOLS:
      return {...state, stacktools: [...action.payload]};
    default:
      return state;
  }
}