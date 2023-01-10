import { vacanciesReducer } from './vacanciesReducer';
import { filterOptionsReducer } from './filterOptionsReducer';
import { countOnPageReducer } from './countOnPageReducer';
import { combineReducers } from 'redux';

export const rootReducer = combineReducers({
  vacanciesReducer,
  filterOptionsReducer,
  countOnPageReducer,
});