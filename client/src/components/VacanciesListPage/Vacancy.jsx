import { React, useContext, useState } from 'react';
import {  
  Box,
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
import { Favorite, ShareOption } from 'grommet-icons';


const VacancyCard = (props) => {
  const size = useContext(ResponsiveContext);
  const navigate = useNavigate();
  const [favorite, setFavorite] = useState(false);
  
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
        
        <Box direction="row" align="center" gap="small">
          <Button primary label="Перейти к вакансии" onClick={() => navigate(`/vacancies/vacancy/${props.id}`)}/>
          <Button icon={<ShareOption color="plain" />} hoverIndicator />
          <Button
            icon={<Favorite color={favorite ? 'red' : undefined} />}
            hoverIndicator
            onClick={() => {
              setFavorite(!favorite);
            }}
          />
        </Box>
      </CardFooter>
    </Card>
  );
};

export default VacancyCard