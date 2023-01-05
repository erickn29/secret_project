import { likesReducer } from './likesReducer';
import { combineReducers } from 'redux';

export const rootReducer = combineReducers({
  likesReducer,
});