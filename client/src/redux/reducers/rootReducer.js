import { vacanciesReducer } from './vacanciesReducer';
import { filterOptionsReducer } from './vacancyFilter/filterOptionsReducer';
import { filterChosenOptionsReducer } from './vacancyFilter/filterChosenOptionsReducer';
import { paginationReducer } from './paginationReducer';
import { combineReducers } from 'redux';

export const rootReducer = combineReducers({
  vacanciesReducer,
  filterOptionsReducer,
  filterChosenOptionsReducer,
  paginationReducer,
});