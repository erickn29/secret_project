import { React, useState, useEffect } from 'react';
import { Select, Button, Sidebar, Avatar } from 'grommet';
import { useSelector, useDispatch } from 'react-redux';
import { fetchFilterValues } from '../../redux/action_creators/vacancyFilters';

import { SET_FILTER_CITY, SET_FILTER_EXPERIENCE, SET_FILTER_GRADE, SET_FILTER_SPECIALITY, SET_FILTER_STACKTOOL, SET_FILTER_VALUE_CLEAR } from "../../redux/types";

const VacancyListFilter = (props) => {
  const { cities, experiences, grades, specialities, stacktools } = useSelector(state => state.filterOptionsReducer);
  const { city, experience, grade, speciality, stacktool } = useSelector(state => state.filterChosenOptionsReducer);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchFilterValues());
  }, []);

  return (
    <form className='vacancy-list-filter'>
        <Select
          options={[...cities]}
          value={city}
          onChange={({ option }) => dispatch({type: SET_FILTER_CITY, payload: option})}
          placeholder="Город..."
        />
      {/* <Select
        options={['Меньше 1 года', 'От 1 до 3 лет', 'Больше 3 лет']}
        value={}
        onChange={({ option }) => setValueExperience(option)}
        placeholder="Опыт..."
      />
      <Select
        options={['Стажер', 'Junior', 'Middle', 'Senior']}
        value={valueGrade}
        onChange={({ option }) => setValueGrade(option)}
        placeholder="Грейд..."
      />
      <Select
        options={[...specialityList]}
        value={valueSpeciality}
        onChange={({ option }) => setValueSpeciality(option)}
        placeholder="Специализация..."
      />
      <Button primary label="Filter" onClick={() => fetchVacanciesByOptions()} /> */}
    </form>
  )
}

export default VacancyListFilter