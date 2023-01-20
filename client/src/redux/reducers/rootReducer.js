import { vacanciesReducer } from './vacanciesReducer';
import { filterOptionsReducer } from './filterOptionsReducer';
import { combineReducers } from 'redux';

export const rootReducer = combineReducers({
  vacanciesReducer,
  filterOptionsReducer,
});