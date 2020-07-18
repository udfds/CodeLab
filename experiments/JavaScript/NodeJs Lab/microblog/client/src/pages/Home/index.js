import React, { useState, useEffect } from 'react';
import axios from 'axios';

import Layout from '../../components/Layout';
import PostForm from '../../components/PostForm';
import PostList from '../../components/PostList';

export default function Home() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const token = localStorage.getItem("SESSION_TOKEN");

        const postsResponse = await axios.get(`${process.env.REACT_APP_SERVER_URL}/posts`, {
            headers: { "auth-token": token }
          }
        );

        const userPosts = await Promise.all(
          postsResponse.data.map(async _post => {
            const user = await axios.get(`${process.env.REACT_APP_SERVER_URL}/users/${_post.owner}`, {
                headers: { "auth-token": token }
              }
            );

            return { ..._post, username: user.data.username };
          })
        );

        setPosts(userPosts);
      } catch (error) {
        console.error(error);
      }
    };

    fetchPosts();
  }, []);

  const onLike = (ownerID, postID) => {
    console.log(ownerID, postID);

    const newPosts = posts.map(_post => {
      if (_post._id === postID) {
        const postLiked = _post.likes.find(owner => owner === ownerID);

        if (postLiked) {
          return {
            ..._post,
            likes: _post.likes.filter(owner => owner !== ownerID)
          };
        }
        return { ..._post, likes: [..._post.likes, ownerID] };
      }
      return _post;
    });

    setPosts(newPosts.reverse());
  };

  const onCreatePost = async content => {
    try {
      const token = localStorage.getItem('SESSION_TOKEN');

      const response = await axios.post(`${process.env.REACT_APP_SERVER_URL}/posts`, {
          content
        },{
          headers: { "auth-token": token }
        }
      );

      setPosts([...posts, response.data]);
    } catch (error) {
      console.error(error);
    }
  };


  return (
    <Layout>
      <PostForm onCreatePost={onCreatePost}></PostForm>
      <PostList posts={posts} onLike={onLike}></PostList>
    </Layout>
  );
}