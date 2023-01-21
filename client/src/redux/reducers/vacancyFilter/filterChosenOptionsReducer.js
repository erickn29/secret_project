import { SET_FILTER_CITY, SET_FILTER_EXPERIENCE, SET_FILTER_GRADE, SET_FILTER_SPECIALITY, SET_FILTER_STACKTOOL, SET_FILTER_VALUE_CLEAR, SET_FILTER_SALARY, SET_FILTER_REMOTE } from "../../types";

const initialState = {
  city: null,
  experience: null,
  grade: null,
  speciality: null,
  stacktool: null,
  chosenSalaryFrom: 0,
  chosenSalaryTo: 300000,
  isRemote: false,
};

export const filterChosenOptionsReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_FILTER_CITY:
      return {...state, city: action.payload};
    case SET_FILTER_EXPERIENCE:
      return {...state, experience: action.payload};
    case SET_FILTER_GRADE:
      return {...state, grade: action.payload};
    case SET_FILTER_SPECIALITY:
      return {...state, speciality: action.payload};
    case SET_FILTER_STACKTOOL:
      return {...state, stacktool: action.payload};
    case SET_FILTER_REMOTE:
      return {...state, isRemote: action.payload};
    case SET_FILTER_SALARY:
      return {...state, chosenSalaryFrom: action.payload.chosenSalaryFrom, chosenSalaryTo: action.payload.chosenSalaryTo};
    case SET_FILTER_VALUE_CLEAR:
      return {...initialState};
    default:
      return state;
  }
}