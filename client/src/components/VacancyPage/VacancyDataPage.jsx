import { React, useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import { Anchor, PageContent, Card, CardHeader, CardBody, CardFooter, Tag, Text, Heading } from 'grommet';
import axios from "axios";


const VacancyDataPage = () => {
  const params = useParams();
  const [vacancyData, setVacancyData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const getVacancyUrl = `http://localhost:8000/vacancies/${params.id}`;
      let response = await axios.get(getVacancyUrl);

      let gotVacancyData = response.data;
      setVacancyData(gotVacancyData);

    }

    fetchData();
  }, [params.id]);

  return (
    <PageContent>
      <Card className="vacancy-card-full" background="light-1">

        {/* Название вакансии */}
        <CardHeader className="vacancy-card-full__header" pad="medium">
          <Heading margin="none">{vacancyData.title}</Heading>
          {/* Дата размещения */}
          {
            vacancyData.date
            ? <Text>Дата размещения: {vacancyData.date}</Text>
            : ''
          }
        </CardHeader>
        
        {/* Данные вакансии */}
        <CardBody pad="medium">




          <Tag name="Специальность" value={vacancyData.speciality} />
          <Tag name="Опыт" value={vacancyData.experience} />
          <Tag name="Grade?" value={vacancyData.grade} />

          {/* Компания вакансии */}
          {
            vacancyData.company
            ? <Text>{vacancyData.company}</Text>
            : ''
          }

          {/* Описание вакансии */}
          <Text>{vacancyData.text}</Text>

          {/* Диапазон зарплат */}
          {(vacancyData.salary_from && vacancyData.salary_to)
            ? <Text>Зарплата: {vacancyData.salary_from} - {vacancyData.salary_to}</Text>
            : (vacancyData.salary_from 
              ? <Text>Зарплата: {vacancyData.salary_from}</Text> : (vacancyData.salary_to 
                ? <Text>Зарплата: {vacancyData.salary_to}</Text> : <Text>Зарплата не указана</Text>))
          }

          {/* Ссылка на вакансию */}
          {
            vacancyData.link ? <Anchor href={vacancyData.link}></Anchor> : ''
          }
            
          {/* Стек */}
          {
            vacancyData.stack 
            ? vacancyData.stack.map((stackItem) => <Tag key={stackItem} value={stackItem} />)
            : ''
          }
          
        </CardBody>

        <CardFooter pad={{horizontal: "small"}} background="light-2">

        </CardFooter>
      </Card>
  </PageContent>
  )
}

export default VacancyDataPage