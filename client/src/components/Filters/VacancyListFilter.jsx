import { React, useState } from 'react';
import { Select } from 'grommet';

const VacancyListFilter = () => {
  const [valueExperience, setValueExperience] = useState('');
  const [valueGrade, setValueGrade] = useState('');
  const [valueSpeciality, setValueSpeciality] = useState('');

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
        options={['Backend', 'Frontend', 'DevOps', 'Machine Learning', 'UI/UX-дизайнер', 'Project Manager', 'Системный администратор', 'QA']}
        value={valueSpeciality}
        onChange={({ option }) => setValueSpeciality(option)}
        placeholder="Специализация..."
      />
    </form>

  )
}

export default VacancyListFilter