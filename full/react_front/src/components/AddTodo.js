import React, { useEffect, useState } from "react";
import TodosContext from '../TodosContext'
function AddTodo() {
    const [item, setItem] = React.useState("")
    const {todos, fetchTodos} = React.useContext(TodosContext)
  
    const handleInput = event  => {
      setItem(event.target.value)
    }
  
    const handleSubmit = (event) => {
      const newTodo = {
        "id": todos.length + 1,
        "item": item
      }
  
      fetch("http://localhost:8000/todo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTodo)
      }).then(fetchTodos)
    }
  
    return (
      <form className="mb-2" style={{ textAlign: "left" }} onSubmit={handleSubmit}>
      <div className="mb-3">
          <input
            pr="4.5rem"
            type="text"
            placeholder="Add a todo item"
            aria-label="Add a todo item"
            onChange={handleInput}
          />
      </div>
      </form>
    )
  }
  export default AddTodo;