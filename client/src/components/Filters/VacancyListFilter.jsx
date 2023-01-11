import { React, useState, useEffect } from 'react';
import { Select, Button } from 'grommet';
import { useSelector, useDispatch } from 'react-redux';
import axios from 'axios';
import { FILTER_CITIES, FILTER_EXPIRIENCES, FILTER_GRADES, FILTER_SPECIALITIES, FILTER_STACKTOOLS } from "../../redux/types";

const VacancyListFilter = (props) => {

  const [selectedCity, setSelectedCity] = useState('');
  const dispatch = useDispatch();
  let citiesInFilter = useSelector(state => state.filterOptionsReducer.cities);

  if (citiesInFilter === undefined) {
    citiesInFilter = [];
  }

  async function fetchFilterOptions(optionName) {
    const optionUrl = `http://localhost:8000/${optionName}`;

    // setIsLoading(true);
    const response = await axios.get(optionUrl);

    const optionResults = response.data.results;

    const action = {type: '', payload: optionResults};

    switch (optionName) {
      // case 'cities':
      //   action.type = FILTER_CITIES;
      //   break;
      case 'cities_by_list':
        const citiesFilterResult = response.data.result;
        action.payload = citiesFilterResult;
        action.type = FILTER_CITIES;
        break;
      case 'experiences':
        action.type = FILTER_EXPIRIENCES;
        break;
      case 'specialities':
        action.type = FILTER_SPECIALITIES;
        break;
      case 'grades':
        action.type = FILTER_GRADES;
        break;
      case 'stacktools':
        action.type = FILTER_STACKTOOLS;
        break;
    }

    dispatch(action);
    // setIsLoading(false);
  }

  useEffect(() => {
    console.log('FETCH START')
    fetchFilterOptions('cities_by_list');
    fetchFilterOptions('specialities');
    fetchFilterOptions('grades');
    fetchFilterOptions('experiences');
    fetchFilterOptions('stacktools');
  }, []);

  return (
    <form className='vacancy-list-filter'>
        <Select
          options={[...citiesInFilter]}
          value={selectedCity}
          onChange={({ option }) => setSelectedCity(option)}
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