<?php

namespace App\Admin\Repositories;

use App\Models\Place as Model;
use Dcat\Admin\Repositories\EloquentRepository;

class Place extends EloquentRepository
{
    /**
     * Model.
     *
     * @var string
     */
    protected $eloquentClass = Model::class;
}
