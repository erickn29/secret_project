import React from 'react';
import VacancyCard from './Vacancy';
import { useSelector } from 'react-redux';

const Vacancies = (props) => {
  const {vacancies, loading, error, page, countOnPage} = useSelector(state => state.vacanciesReducer);

  // const generateVacanciesMock = () => {
  //   let result = [];
  //   for (let i = 0; i < 10; i++) {
  //     result.push(<VacancyCard key={i} isMock={true}></VacancyCard>);
  //   }

  //   return result;
  // }

  // let vacanciesList
  // props.isLoading
  // ? vacanciesList = generateVacanciesMock()
  // : 
  const vacanciesList = vacancies.map((vacancy) => <VacancyCard key={vacancy.id} {...vacancy}></VacancyCard>)

  return (
    <section className="vacancies">
        {vacanciesList}
    </section>
  )
}

export default Vacancies