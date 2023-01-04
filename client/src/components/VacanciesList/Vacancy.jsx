import { React, useContext } from 'react';
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
} from 'grommet';

const VacancyCard = (props) => {
  const size = useContext(ResponsiveContext);

  return (
    <Card className='vacancy-card'>
      <CardHeader pad="medium">
        <Heading level={2} margin="none">
          {props.title}
        </Heading>
      </CardHeader>
      <CardBody pad="medium">
        <Paragraph maxLines={size === "small" ? 3 : undefined}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
          porttitor non nulla ac vehicula. Aliquam erat volutpat. Mauris auctor
          faucibus est at mattis. Aliquam a enim ac nisi aliquam consectetur et
          ac velit. Mauris ut imperdiet libero.
        </Paragraph>
      </CardBody>
      <CardFooter pad="medium" background="background-contrast">
        <Button
          primary
          label="Go to vacancy"
          active
          onClick={() => {}}
          {...props}
        />
      </CardFooter>
    </Card>
  );
};

export default VacancyCard