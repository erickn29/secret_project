import React from "react";
import { PageContent, Box, Carousel, Image, Paragraph } from "grommet";

const MainPage = () => {
  return (
    <PageContent>
      <Box className="main-content__carousel" alignSelf="center" height="medium" width="xxlarge" overflow="hidden">
        <Carousel fill>
          <Image fit="cover" src="https://o6u.edu.eg/images/pages/10112022080426%D8%B5499.jpg" />
          <Image fit="cover" src="https://www.gu.edu.eg/wp-content/uploads/2022/06/black-male-in-front-of-computer-screen-coding-mobi-2021-08-29-08-49-00-utc-901x365.jpg" />
          <Image fit="cover" src="http://static1.squarespace.com/static/5269fbd3e4b0eb2b76ccc1db/54bc1ff5e4b0276f663b2dd7/5f4fe6c2faea81233cb2cb0a/1665762483046/best-computer-science-schools_REV.jpg?format=1500w" />
        </Carousel>
      </Box>
      <div className="main-content__description">
        <Paragraph>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Hic architecto et, explicabo nihil obcaecati eligendi a perspiciatis 
        </Paragraph>
        <Paragraph>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Hic architecto et, explicabo nihil obcaecati eligendi a perspiciatis libero minima aut dolorem quam minus voluptate nemo doloremque voluptatum, sed rerum accusamus cupiditate sint. Voluptatibus 
        </Paragraph>
        <Paragraph>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Hic architecto et, explicabo nihil obcaecati eligendi a perspiciatis libero minima aut dolorem quam minus voluptate nemo doloremque voluptatum, sed rerum accusamus cupiditate sint. Voluptatibus taque quisquam perferendis error, at blanditiis dolor distinctio, quos corporis dolores quam corrupti magnam amet fugiat.
        </Paragraph>
      </div>
    </PageContent>
  );
};

export default MainPage;
