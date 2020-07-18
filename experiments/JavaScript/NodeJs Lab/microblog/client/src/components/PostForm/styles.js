import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  padding: 1rem;
  border: 1px solid #cccccc;

  > textarea {
    resize: none;
    margin-bottom: 1rem;
    color: #4f9e64;
    border: 1px solid #4f9e64;
    border-radius: 10px;
  }

  > div {
    display: flex;
    justify-content: flex-end;

    > button {
      background: white;
      border: 1px solid #4f9e64;
      padding: 0.4rem 1rem;
      border-radius: 20px;
      color: #4f9e64;
      font-weight: 600;
      cursor: pointer;

      &:hover {
        background: #4f9e64;
        color: white;
      }

    }

  }
`;