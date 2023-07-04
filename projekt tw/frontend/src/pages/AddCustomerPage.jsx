import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useState } from "react";
import "./AddCustomerPage.css"
import { json } from "react-router-dom";

export const AddCustomerPage = () => {
  const[name, setName] = useState("")
  const[surname, setSurame] = useState("")
  const[email, setEmail] = useState("")
  const[phone_number, setPhone_number] = useState("")

  const submitFormHandler = (event) => {
    event.preventDefault()
    fetch("http://127.0.0.1:8000/customers/", {
      method: "POST",
      headers: {"Content-Type" : "application/json"},
      body: JSON.stringify({"name": name, "surname": surname, "email": email, "phone_number": phone_number})
    }).then((res) => res.json())
    .then((data) => console.log(data))

    setName("");
    setSurame("");
    setEmail("");
    setPhone_number("");
  }
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
        <form className="add_customer">
          <input type="text" placeholder="Name" value={name} onChange={(event) => setName(event.target.value)} required/>
          <input type="text" placeholder="Surname" value={surname} onChange={(event) => setSurame(event.target.value)} required/>
          <input type="text" placeholder="Email address" value={email} onChange={(event) => setEmail(event.target.value)} required/>
          <input type="text" placeholder="Phone number" value={phone_number} onChange={(event) => setPhone_number(event.target.value)} required/>
          <button className="form" type="submit" onClick={submitFormHandler}>Add customer</button>
        </form>
      </div>
    </div>
  );
};
