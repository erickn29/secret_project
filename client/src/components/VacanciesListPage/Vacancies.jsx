import React from 'react';
import VacancyCard from './Vacancy';
import { Routes, Route } from 'react-router-dom';

const Vacancies = ({vacancies}) => {
  const vacanciesList = vacancies.map((vacancy) => <VacancyCard key={vacancy.id} {...vacancy}></VacancyCard>)

  return (
    <section className="vacancies">
        {vacanciesList}
    </section>
  )
}

export default Vacancies