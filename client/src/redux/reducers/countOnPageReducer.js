import { COUNT_ON_PAGE_10, COUNT_ON_PAGE_30, COUNT_ON_PAGE_50 } from "../types";

const initialState = {
  countOnPage: 10,
};

export const countOnPageReducer = (state = initialState, action) => {

  switch (action.type) {
    case COUNT_ON_PAGE_10:
      return { countOnPage: 10, };
    case COUNT_ON_PAGE_30:
      return { countOnPage: 30, };
    case COUNT_ON_PAGE_50:
      return { countOnPage: 50, };
    default:
      return state;
  }
}