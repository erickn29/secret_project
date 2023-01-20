import { vacanciesReducer } from './vacanciesReducer';
import { filterOptionsReducer } from './filterOptionsReducer';
import { paginationReducer } from './paginationReducer';
import { combineReducers } from 'redux';

export const rootReducer = combineReducers({
  vacanciesReducer,
  // filterOptionsReducer,
  paginationReducer,
});