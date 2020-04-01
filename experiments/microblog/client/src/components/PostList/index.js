import React from 'react';

import { Container } from './styles';
import Post from "../Post";

export default function PostList(props) {
    return (
        <Container>
            <ul>
                {props.posts.reverse().map(post => (
                    <Post
                        key={post._id}
                        tweetId={post._id}
                        owner={post.owner}
                        username={post.username}
                        content={post.content}
                        likes={post.likes.length}
                        onLike={props.onLike}
                    />
                ))}
            </ul>
        </Container>
    );
}