import { GENERAL_VACANCIES } from "../types";

const initialState = [];


export const vacanciesReducer = (state = initialState, action) => {

  switch (action.type) {
    case GENERAL_VACANCIES:
      return [...action.payload];
    default:
      return state;
  }
}