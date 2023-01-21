import { PAGINATION_SET_COUNT_ON_PAGE, PAGINATION_SET_PAGE } from "../types";

const initialState = {
  page: 1,
  countOnPage: 10,
}

export const paginationReducer = (state = initialState, action) => {
  switch (action.type) {
    case PAGINATION_SET_COUNT_ON_PAGE:
      return {
        ...state,
        countOnPage: action.payload,
      };
    case PAGINATION_SET_PAGE:
      return {
        ...state,
        page: action.payload,
      };
    default:
      return {...state};
  }
}