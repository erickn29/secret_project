import React from 'react';
import { INCREMENT, DECREMENT } from '../redux/types';
import { connect } from 'react-redux';

const Likes = (props) => {
  return (
    <div>Likes = { props.likes }
      <button onClick={ props.onIncrementLikes }>Like</button>
      <button onClick={ props.onDecrementLikes } >Dislike</button>
    </div>
  )
}

function mapStateToProps(state) {
  const { likesReducer } = state;
  return { 
    likes: likesReducer.likes,
  }
}

function mapDispatchToProps(dispatch) {
  return {
    onIncrementLikes: () => {
      const action = { type: INCREMENT};
      dispatch(action);
    },
    onDecrementLikes: () => {
      const action = { type: DECREMENT};
      dispatch(action);
    },
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Likes);