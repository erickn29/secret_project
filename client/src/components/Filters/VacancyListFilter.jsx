import { React, useState, useEffect } from 'react';
import { Select, Button, Sidebar, Avatar, TextInput, RangeSelector, Stack, Box, Text, CheckBox } from 'grommet';
import { useSelector, useDispatch } from 'react-redux';
import { fetchFilterValues } from '../../redux/action_creators/vacancyFilters';

import { SET_FILTER_CITY, SET_FILTER_EXPERIENCE, SET_FILTER_GRADE, SET_FILTER_SPECIALITY, SET_FILTER_STACKTOOL, SET_FILTER_VALUE_CLEAR, SET_FILTER_SALARY, SET_FILTER_REMOTE } from "../../redux/types";

const VacancyListFilter = (props) => {
  const { cities, experiences, grades, specialities, stacktools, salaryFrom, salaryTo, salaryStep } = useSelector(state => state.filterOptionsReducer);
  const { city, experience, grade, speciality, stacktool, chosenSalaryFrom, chosenSalaryTo, isRemote } = useSelector(state => state.filterChosenOptionsReducer);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchFilterValues());
  }, []);

  const getSalariesRangeValues = (salaryFrom, salaryTo, salaryStep) => {
    const salariesValues = [];
    
    for (let i = salaryFrom; i < salaryTo; i += salaryStep) {
      salariesValues.push(i);
    }

    return salariesValues;
  }


  return (
    <form className='vacancy-list-filter'>
      <div className='filter-row'>
        <TextInput
          placeholder="Город..."
          value={city}
          onChange={(event) => dispatch({type: SET_FILTER_CITY, payload: event.target.value})}
          list="cities-filter-list"
        />
        <datalist id="cities-filter-list">
          {cities.map((city, index) => {
            return <option key={city} value={city}></option>
          })}
        </datalist>

      </div>



      <Stack>
        <Box direction="row" justify="between">
          {getSalariesRangeValues(salaryFrom, salaryTo, salaryStep).map(value => (
            <Box key={value} pad="small" border={false}>
              <Text style={{ fontFamily: 'monospace' }}>
                {value}
              </Text>
            </Box>
          ))}
        </Box>
        <RangeSelector
          direction="horizontal"
          invert={false}
          min={salaryFrom}
          max={salaryTo}
          size="full"
          round="small"
          step={salaryStep}
          values={[chosenSalaryFrom, chosenSalaryTo]}
          onChange={values => dispatch({type: SET_FILTER_SALARY, payload: {
            chosenSalaryFrom: values[0],
            chosenSalaryTo: values[1],
          }})}
        />
      </Stack>

      <CheckBox
        checked={isRemote}
        label="Удаленная?"
        onChange={(event) => dispatch({type: SET_FILTER_REMOTE, payload: !isRemote})}
      />




      {/* <Select
        options={[...cities]}
        value={city}
        onChange={({ option }) => dispatch({type: SET_FILTER_CITY, payload: option})}
        placeholder="Город..."
      /> */}
    </form>
  )
}

export default VacancyListFilter