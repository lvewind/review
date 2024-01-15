<?php

namespace App\Admin\Repositories;

use App\Models\Inspector as Model;
use Dcat\Admin\Repositories\EloquentRepository;

class Inspector extends EloquentRepository
{
    /**
     * Model.
     *
     * @var string
     */
    protected $eloquentClass = Model::class;
}
