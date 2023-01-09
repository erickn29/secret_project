import { React, useState, useEffect } from 'react';
import { Select, Button } from 'grommet';

const VacancyListFilter = (props) => {
  const [valueExperience, setValueExperience] = useState([]);
  const [valueGrade, setValueGrade] = useState([]);
  const [valueSpeciality, setValueSpeciality] = useState([]);
  const [valueCity, setValueCity] = useState([]);

  const [cityList, setCityList] = useState([]);
  const [specialityList, setSpecialityList] = useState([]);

  async function fetchFilterOptions(optionName) {
    const optionUrl = `http://localhost:8000/${optionName}`;
    
    setIsLoading(true);
    let response = await axios.get(optionUrl);

    let optionResults = response.data.results;

    if (optionName === 'cities') {
      setCityList(optionResults);
    } else if (optionName === 'specialities') {
      setSpecialityList(optionResults);
    }

    setIsLoading(false);
  }

  async function fetchVacanciesByOptions() {
    const vacanciesByOptionUrl = `http://localhost:8000/vacancies/search`;
    
    setIsLoading(true);
    let response = await axios.get(optionUrl, { params: { answer: 42 } });

    let vacanciesByOption = response.data.results;
    props.setVacancies(vacanciesByOption);
    props.setVacanciesCount(vacanciesByOption.length);

    setIsLoading(false);
  }

  useEffect(() => {
    fetchFilterOptions('cities');
    fetchFilterOptions('specialities');
  }, []);

  return (
    <form className='vacancy-list-filter'>
      <Select
        options={['Меньше 1 года', 'От 1 до 3 лет', 'Больше 3 лет']}
        value={valueExperience}
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
      <Select
        options={[...cityList]}
        value={valueSpeciality}
        onChange={({ option }) => setValueSpeciality(option)}
        placeholder="Город..."
      />
      <Button primary label="Filter" onClick={() => fetchVacanciesByOptions()} />
    </form>
  )
}

export default VacancyListFilter