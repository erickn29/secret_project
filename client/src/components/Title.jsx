import React from 'react'

const Title = () => {
  const handleChange = (event) => {
    console.log(event.target.value);
  }

  return (
    <div className='card-title'>
      <div className='card-title-top'>
        <input type="text" onChange={handleChange}/>
      </div>
    </div>
  )
}

export default Title