import React, { useEffect, useState } from "react";
import AddTodo from './AddTodo'
import RenderTodo from './RenderTodo';
import TodosContext from '../TodosContext'
/* const TodosContext = React.createContext({
  todos: [], fetchTodos: () => {}
}) */

export default function Todos() {
  const [todos, setTodos] = useState([])
  const fetchTodos = async () => {
    const response = await fetch("http://localhost:8000/todo")
    const todos = await response.json()
    setTodos(todos.data)
  }
  useEffect(() => {
    fetchTodos()
  }, [])
  return (
    <TodosContext.Provider value={{todos, fetchTodos}}>
    <AddTodo /> 
        {todos.map((todo) => (
          <b>{todo.item}</b>
        ))}
        {
        todos.map((todo) => (
          <RenderTodo item={todo.item} id={todo.id} fetchTodos={fetchTodos} />
        ))
      }
    </TodosContext.Provider>
  )
}