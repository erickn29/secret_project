import { React, useContext } from 'react';
import {  
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  ResponsiveContext,
  Heading,
  Paragraph,
  Skeleton,
} from 'grommet';
import { useNavigate } from 'react-router-dom';


const VacancyCard = (props) => {
  const size = useContext(ResponsiveContext);
  const navigate = useNavigate();
  
  return (
    <Card className='vacancy-card'>
      <CardHeader pad="medium">
        <Heading level={2} margin="none">
          {
            props.isMock
            ? <Skeleton />
            : props.title
          }
        </Heading>
      </CardHeader>
      <CardBody pad="medium">
      {
        props.isMock
        ? <Skeleton />
        : <Paragraph maxLines={size === "small" ? 3 : undefined}>Опыт: {props.experience ? props.experience : "Не указано"}<br/>Грейд: {props.grade ? props.grade : "Не указано"}<br/>Компания: {props.company ? props.company : "Не указано"}</Paragraph>
      }
      </CardBody>
      <CardFooter pad="medium" background="background-contrast">
        <Button primary label="Перейти к вакансии" onClick={() => navigate(`/vacancies/vacancy/${props.id}`)}/>
      </CardFooter>
    </Card>
  );
};

export default VacancyCard