import React from 'react';

function SearchBar({ search, handleSearchChange }) {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search by name, car type or description..."
        value={search}
        onChange={handleSearchChange}
      />
    </div>
  );
}

export default SearchBar;
