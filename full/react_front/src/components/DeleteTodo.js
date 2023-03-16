import React, { useEffect, useState } from "react";
import TodosContext from '../TodosContext'
function DeleteTodo({id}) {
    const {fetchTodos} = React.useContext(TodosContext)
  
    const deleteTodo = async () => {
      await fetch(`http://localhost:8000/todo/${id}`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: { "id": id }
      })
      await fetchTodos()
    }
  
    return (
      <button h="1.5rem" size="sm" onClick={deleteTodo}>Delete Todo</button>
    )
  }
  export default DeleteTodo;